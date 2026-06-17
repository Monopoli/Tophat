import os

folder = r"C:\Users\etkma\Downloads\BlamScript-Research-master\BlamScript-Research-master\h2v\01b_spacestation"

for filename in os.listdir(folder):
    if filename.lower().endswith(".lisp"):
        src = os.path.join(folder, filename)
        dst = os.path.join(folder, filename[:-5] + ".txt")

        with open(src, "rb") as f_in:      # read raw bytes
            data = f_in.read()

        with open(dst, "wb") as f_out:     # write raw bytes
            f_out.write(data)

        print(f"Converted {filename} → {os.path.basename(dst)}")
