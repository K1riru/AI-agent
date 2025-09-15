import os
def get_files_info(working_directory, directory="."):
    try:
        root_abs = os.path.abspath(working_directory)
        target_abs = os.path.abspath(os.path.join(working_directory,directory))

        if not (target_abs == root_abs or target_abs.startswith(root_abs + os.sep)):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(target_abs):
            return f'Error: "{directory}" is not a directory'
   

        lines = []
        for name in os.listdir(target_abs):
            item_path = os.path.join(target_abs, name)
            size = os.path.getsize(item_path)
            is_dir = os.path.isdir(item_path)
            lines.append(f'- {name}: file_size={size} bytes, is_dir={is_dir}')

        return "\n".join(lines)

    except Exception as e:
        return f"Error: {e}"
    