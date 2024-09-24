import os
import subprocess

def run_command(commmand):
    # Запускает системную команду
    result = subprocess.run(commmand, shell=True, text=True)
    return result

def install_neovim_config(repo_url, config_dir):
    # Клонирует репозиторий с Neovim
    print("Клонирование конфигурации Neovim...")
    if not os.path.exists(config_dir):
        run_command(f"git clone {repo_url} {config_dir}")
    else:
        print("Конфигурация уже существует, обновление репозитория...")
        run_command(f"cd {config_dir} && git pull")

def main():
    repo_url = "https://github.com/AoiIT/Alarivim.git"

    # Директория для конфига Neovim
    config_dir = os.path.expanduser("~/.config/nvim")

    install_neovim_config(repo_url, config_dir)
    print("Конфигурация Neovim успешно установлена!")

if __name__ == "__main__":
    main()
