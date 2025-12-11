#!/usr/bin/env python3
"""
Instagram Reel Downloader using yt-dlp
Alternative method that's often more reliable than instaloader
"""

import subprocess
import sys
import os
from pathlib import Path

# Import credentials from credentials.py
try:
    from credentials import INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD
except ImportError:
    print("Error: credentials.py file not found!")
    print("\nPlease create a credentials.py file with your Instagram credentials:")
    print("=" * 60)
    print("# credentials.py")
    print("INSTAGRAM_USERNAME = 'your_username'")
    print("INSTAGRAM_PASSWORD = 'your_password'")
    print("=" * 60)
    sys.exit(1)


def check_ytdlp_installed():
    """Check if yt-dlp is installed"""
    try:
        result = subprocess.run(['yt-dlp', '--version'], 
                              capture_output=True, text=True, timeout=5)
        return result.returncode == 0
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return False


def download_with_ytdlp(reel_url, output_dir="downloads"):
    """
    Download Instagram reel using yt-dlp
    
    Args:
        reel_url (str): URL of the Instagram reel
        output_dir (str): Directory to save the downloaded reel
    """
    # Validate credentials
    if not INSTAGRAM_USERNAME or INSTAGRAM_USERNAME == "your_username_here":
        print("Error: Please update INSTAGRAM_USERNAME in credentials.py")
        return False
    
    if not INSTAGRAM_PASSWORD or INSTAGRAM_PASSWORD == "your_password_here":
        print("Error: Please update INSTAGRAM_PASSWORD in credentials.py")
        return False
    
    # Check if yt-dlp is installed
    if not check_ytdlp_installed():
        print("Error: yt-dlp is not installed!")
        print("\nInstall it with:")
        print("  pip install yt-dlp")
        print("or")
        print("  pip install -U yt-dlp")
        return False
    
    # Create output directory
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    # Build yt-dlp command
    output_template = os.path.join(output_dir, "%(uploader)s_%(id)s.%(ext)s")
    
    cmd = [
        'yt-dlp',
        '--username', INSTAGRAM_USERNAME,
        '--password', INSTAGRAM_PASSWORD,
        '--output', output_template,
        '--format', 'best',
        '--no-playlist',
        '--user-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        reel_url
    ]
    
    print(f"Downloading reel from: {reel_url}")
    print(f"Output directory: {output_dir}")
    print("-" * 60)
    print("Using yt-dlp to download...")
    print()
    
    try:
        # Run yt-dlp
        result = subprocess.run(cmd, check=True)
        
        if result.returncode == 0:
            print()
            print("✓ Successfully downloaded reel!")
            return True
        else:
            print(f"\n✗ Download failed with exit code: {result.returncode}")
            return False
            
    except subprocess.CalledProcessError as e:
        print(f"\n✗ Download failed: {e}")
        print("\nTroubleshooting tips:")
        print("1. Make sure your credentials in credentials.py are correct")
        print("2. Check if the reel URL is valid")
        print("3. The reel might be private or deleted")
        print("4. Try updating yt-dlp: pip install -U yt-dlp")
        return False
    except Exception as e:
        print(f"\n✗ Unexpected error: {e}")
        return False


def main():
    """Main function"""
    if len(sys.argv) < 2:
        print("Instagram Reel Downloader (yt-dlp method)")
        print("=" * 60)
        print("\nThis is an alternative downloader using yt-dlp")
        print("Often more reliable than instaloader!")
        print()
        print("Setup:")
        print("  1. Install yt-dlp: pip install yt-dlp")
        print("  2. Edit credentials.py with your Instagram credentials")
        print("  3. Run the script:")
        print(f"     python {sys.argv[0]} <reel_url> [output_directory]")
        print("\nExamples:")
        print(f"  python {sys.argv[0]} https://www.instagram.com/reel/ABC123/")
        print(f"  python {sys.argv[0]} https://www.instagram.com/reel/ABC123/ my_reels")
        sys.exit(1)
    
    reel_url = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "downloads"
    
    success = download_with_ytdlp(reel_url, output_dir)
    
    if not success:
        sys.exit(1)
    
    print(f"\nFiles saved in: {output_dir}/")


if __name__ == "__main__":
    main()