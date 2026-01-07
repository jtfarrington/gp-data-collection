"""
MPV Installation Script for Windows
Automatically downloads and installs MPV for video synchronization
"""

import os
import sys
import urllib.request
import zipfile
import shutil
import subprocess
from pathlib import Path


def is_admin():
    """Check if running with administrator privileges"""
    try:
        import ctypes
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def check_mpv_installed():
    """Check if MPV is already installed"""
    mpv_path = r"C:\Program Files\mpv\mpv.exe"
    
    if os.path.exists(mpv_path):
        print(f"MPV already installed at: {mpv_path}")
        return True
    
    # Check if in PATH
    try:
        result = subprocess.run(['mpv', '--version'], 
                              capture_output=True, 
                              text=True)
        if result.returncode == 0:
            print("MPV found in system PATH")
            return True
    except:
        pass
    
    return False


def download_mpv():
    """Download MPV from official source"""
    print("\nDownloading MPV...")
    
    # MPV download URL (shinchiro builds - known to have IPC)
    # This is a stable build URL
    url = "https://sourceforge.net/projects/mpv-player-windows/files/64bit/mpv-x86_64-20241229-git-6e542d1.7z/download"
    
    download_path = "mpv_download.7z"
    
    try:
        print(f"Downloading from: {url}")
        urllib.request.urlretrieve(url, download_path)
        print(f"Downloaded to: {download_path}")
        return download_path
    except Exception as e:
        print(f"Download failed: {e}")
        return None


def extract_mpv(archive_path):
    """Extract MPV archive"""
    print("\nExtracting MPV...")
    
    # Check if 7-Zip is installed
    seven_zip_paths = [
        r"C:\Program Files\7-Zip\7z.exe",
        r"C:\Program Files (x86)\7-Zip\7z.exe"
    ]
    
    seven_zip = None
    for path in seven_zip_paths:
        if os.path.exists(path):
            seven_zip = path
            break
    
    if not seven_zip:
        print("7-Zip not found!")
        print("Please install 7-Zip from: https://www.7-zip.org/")
        print("Then run this script again.")
        return None
    
    # Extract to temp directory
    temp_dir = "mpv_temp"
    os.makedirs(temp_dir, exist_ok=True)
    
    try:
        subprocess.run([seven_zip, 'x', archive_path, f'-o{temp_dir}', '-y'],
                      check=True)
        print(f"Extracted to: {temp_dir}")
        return temp_dir
    except Exception as e:
        print(f"Extraction failed: {e}")
        return None


def install_mpv(extracted_dir):
    """Install MPV to Program Files"""
    print("\nInstalling MPV...")
    
    install_path = r"C:\Program Files\mpv"
    
    # Find the mpv folder in extracted directory
    # The archive usually has a subfolder
    mpv_folder = None
    for item in os.listdir(extracted_dir):
        item_path = os.path.join(extracted_dir, item)
        if os.path.isdir(item_path):
            # Check if this folder contains mpv.exe
            if os.path.exists(os.path.join(item_path, 'mpv.exe')):
                mpv_folder = item_path
                break
    
    if not mpv_folder:
        print("Could not find mpv.exe in extracted files")
        return False
    
    # Copy to Program Files
    try:
        if os.path.exists(install_path):
            print(f"Removing existing installation at {install_path}")
            shutil.rmtree(install_path)
        
        shutil.copytree(mpv_folder, install_path)
        print(f"Installed to: {install_path}")
        return True
    except Exception as e:
        print(f"Installation failed: {e}")
        print("Make sure you're running as Administrator")
        return False


def add_to_path():
    """Add MPV to system PATH"""
    print("\nAdding MPV to PATH...")
    
    mpv_path = r"C:\Program Files\mpv"
    
    try:
        # Use PowerShell to add to PATH
        ps_command = f"""
        $path = [Environment]::GetEnvironmentVariable('Path', 'Machine')
        if ($path -notlike '*{mpv_path}*') {{
            [Environment]::SetEnvironmentVariable('Path', "$path;{mpv_path}", 'Machine')
            Write-Output 'Added to PATH'
        }} else {{
            Write-Output 'Already in PATH'
        }}
        """
        
        result = subprocess.run(['powershell', '-Command', ps_command],
                              capture_output=True,
                              text=True)
        
        print(f"✓ {result.stdout.strip()}")
        return True
    except Exception as e:
        print(f"Could not add to PATH automatically: {e}")
        print("\nManual PATH setup:")
        print(f"1. Press Win + R")
        print(f"2. Type: sysdm.cpl")
        print(f"3. Click 'Environment Variables'")
        print(f"4. Edit 'Path' in System Variables")
        print(f"5. Add: {mpv_path}")
        return False


def verify_installation():
    """Verify MPV installation"""
    print("\nVerifying installation...")
    
    mpv_path = r"C:\Program Files\mpv\mpv.exe"
    
    if not os.path.exists(mpv_path):
        print("✗ mpv.exe not found")
        return False
    
    try:
        result = subprocess.run([mpv_path, '--version'],
                              capture_output=True,
                              text=True)
        if result.returncode == 0:
            print("MPV installed successfully!")
            print(f"\nVersion info:\n{result.stdout[:200]}")
            return True
    except Exception as e:
        print(f"Verification failed: {e}")
    
    return False


def cleanup(files_to_remove):
    """Clean up temporary files"""
    print("\n🧹 Cleaning up...")
    
    for file_path in files_to_remove:
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
            print(f"Removed: {file_path}")
        except Exception as e:
            print(f"Could not remove {file_path}: {e}")


def main():
    """Main installation process"""
    print("="*60)
    print("MPV Video Player Installation Script")
    print("="*60)
    
    # Check admin privileges
    if not is_admin():
        print("\nThis script requires Administrator privileges")
        print("Please right-click and 'Run as Administrator'")
        input("\nPress Enter to exit...")
        sys.exit(1)
    
    # Check if already installed
    if check_mpv_installed():
        response = input("\nMPV is already installed. Reinstall? (y/n): ")
        if response.lower() != 'y':
            print("Installation cancelled")
            return
    
    temp_files = []
    
    try:
        # Download
        archive = download_mpv()
        if not archive:
            return
        temp_files.append(archive)
        
        # Extract
        extracted = extract_mpv(archive)
        if not extracted:
            return
        temp_files.append(extracted)
        
        # Install
        if not install_mpv(extracted):
            return
        
        # Add to PATH
        add_to_path()
        
        # Verify
        if verify_installation():
            print("\n" + "="*60)
            print("Installation Complete!")
            print("="*60)
            print("\nImportant: Restart your terminal/IDE for PATH changes to take effect")
        
    except KeyboardInterrupt:
        print("\n\nInstallation cancelled by user")
    except Exception as e:
        print(f"\n\nInstallation failed: {e}")
        import traceback
        traceback.print_exc()
    finally:
        # Cleanup
        cleanup(temp_files)
        input("\nPress Enter to exit...")


if __name__ == "__main__":
    main()