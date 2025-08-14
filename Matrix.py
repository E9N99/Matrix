import os
import subprocess
import base64


Matrix = "aHR0cHM6Ly9naXRodWIuY29tL0U5Tjk5L2F5YS5naXQ="

افتراضية
BiLaL = os.getenv("MATRIX_BRANCH", "main")

def run(cmd):
    print(f"⌭ تنفيذ: {cmd}")
    subprocess.run(cmd, shell=True, check=True)

def _run_git_clone():
    print("• جـاري تحميل سورس ماتركـس.....")
    
    repo_matrix = base64.b64decode(Matrix.replace(" ", "")).decode()
    
    run(f"git clone -b {BiLaL} {repo_matrix} source_temp")
    os.chdir("source_temp")

def _install_requirements():
    print("⌭ تثبيت مكاتب ماتركـس ⌭")
    run("pip install -r requirements.txt")

def _start_project():
    print("⌭ البدء بتشغيل ماتركـس ⌭")
    run("python3 server.py &")
    run("python3 -m zelz")

if __name__ == "__main__":
    _run_git_clone()
    _install_requirements()
    _start_project()
