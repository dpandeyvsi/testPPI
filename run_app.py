import subprocess


if __name__ == "__main__":
    index_url = 'https://127.0.0.1:5000/'
    edge_path = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
    subprocess.Popen([edge_path, index_url])
    subprocess.run(["python", "app.py"])
