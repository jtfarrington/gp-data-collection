"""
Video Controller for MPV Integration
Manages MPV process and IPC communication
"""

import subprocess
import win32file
import json
import time
import os


class VideoController:
    """Manages MPV video player via IPC"""
    
    def __init__(self):
        self.mpv_process = None
        self.pipe_handle = None
        self.mpv_path = r"C:\Program Files\mpv\mpv.exe"
        self.pipe_path = r'\\.\pipe\pipe\mpvsocket'
        self.current_video_path = None
        
    def is_mpv_available(self):
        """Check if MPV is installed"""
        return os.path.exists(self.mpv_path)
    
    def start_mpv(self, video_path):
            """
            Start MPV with IPC enabled
            
            Args:
                video_path: Full path to video file
                
            Returns:
                True if successful, False otherwise
            """
            if not os.path.exists(video_path):
                print(f"✗ Video file not found: {video_path}")
                return False
            
            if not self.is_mpv_available():
                print(f"✗ MPV not found at: {self.mpv_path}")
                return False
            
            # Close existing MPV if running
            if self.mpv_process:
                self.stop_mpv()
            
            try:
                # Start MPV process
                self.mpv_process = subprocess.Popen([
                    self.mpv_path,
                    video_path,
                    '--input-ipc-server=//./pipe/mpvsocket',
                    '--pause',
                    '--keep-open=yes'
                ])
                
                self.current_video_path = video_path
                
                # Wait a moment for MPV to start
                time.sleep(1)
                
                # Connect to pipe
                self._connect_to_pipe()
                
                print(f"✓ MPV started with video: {os.path.basename(video_path)}")
                return True
                
            except Exception as e:
                print(f"✗ Error starting MPV: {e}")
                import traceback
                traceback.print_exc()
                return False
    
    def _connect_to_pipe(self):
        """Connect to MPV's IPC pipe"""
        try:
            self.pipe_handle = win32file.CreateFile(
                self.pipe_path,
                win32file.GENERIC_READ | win32file.GENERIC_WRITE,
                0,
                None,
                win32file.OPEN_EXISTING,
                0,
                None
            )
            print("✓ Connected to MPV pipe")
        except Exception as e:
            print(f"✗ Failed to connect to pipe: {e}")
            self.pipe_handle = None
    
    def _send_command(self, command):
            """Send command to MPV"""
            if not self.pipe_handle:
                return False
            
            try:
                message = (json.dumps(command) + '\n').encode()
                win32file.WriteFile(self.pipe_handle, message)
                return True
                
            except Exception as e:
                print(f"✗ Command failed: {e}")
                # Pipe might be broken
                self.pipe_handle = None
                return False
    
    def seek_to_timestamp(self, seconds):
            """
            Seek video to specific timestamp
            
            Args:
                seconds: Time in seconds (int or float)
                
            Returns:
                True if successful
            """
            # Ensure connected
            if not self._ensure_connected():
                print("✗ Not connected to MPV")
                return False
            
            try:
                success = self._send_command({"command": ["seek", seconds, "absolute"]})
                if success:
                    print(f"✓ Seeked to {seconds}s")
                return success
            except Exception as e:
                print(f"✗ Seek failed: {e}")
                import traceback
                traceback.print_exc()
                return False
    
    def set_pause(self, paused):
        """
        Set pause state
        
        Args:
            paused: True to pause, False to play
            
        Returns:
            True if successful
        """
        success = self._send_command({"command": ["set_property", "pause", paused]})
        if success:
            state = "paused" if paused else "playing"
            print(f"✓ Set to {state}")
        return success
    
    def stop_mpv(self):
        """Stop MPV and cleanup"""
        # Close pipe
        if self.pipe_handle:
            try:
                win32file.CloseHandle(self.pipe_handle)
            except:
                pass
            self.pipe_handle = None
        
        # Terminate process
        if self.mpv_process:
            try:
                self.mpv_process.terminate()
                self.mpv_process.wait(timeout=3)
            except:
                self.mpv_process.kill()
            self.mpv_process = None
        
        self.current_video_path = None
        print("✓ MPV stopped")

    def _ensure_connected(self):
        """Ensure pipe is connected, reconnect if needed"""
        if not self.pipe_handle and self.mpv_process:
            print("Pipe disconnected, attempting to reconnect...")
            try:
                self._connect_to_pipe()
            except:
                print("✗ Failed to reconnect pipe")
                return False
        return self.pipe_handle is not None