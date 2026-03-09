import qrcode
import os

def qr_generate():
    # PARAMETERS
    target_url = "https://emresezer.space" 
    file_name = "website.png"
    
    print(f"System: Process initiated for {target_url}...")

    try:
        # QR Configuration
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=15, # Increased box_size for higher resolution
            border=4,
        )
        
        qr.add_data(target_url)
        qr.make(fit=True)

        # Image Synthesis
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Save the file
        img.save(file_name)
        
        # Absolute path retrieval
        full_path = os.path.abspath(file_name)
        print("\n" + "="*30)
        print("SYSTEM REPORT: SUCCESS")
        print(f"File Name: {file_name}")
        print(f"Full Path: {full_path}")
        print("="*30)
        print("QR Code has been successfully rendered.")

    except Exception as e:
        print(f"\n[ERROR]: A system failure occurred: {e}")

if __name__ == "__main__":
    qr_generate()
