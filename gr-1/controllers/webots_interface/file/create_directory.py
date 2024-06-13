import os

# 定义基础目录
base_directory = "SonnieControl/upbody/ArmControl/file/custom_motion_set"

# 创建100个子目录
for i in range(1, 101):
    sub_directory = os.path.join(base_directory, f"motion_{i}")
    os.makedirs(sub_directory)

    # 在每个子目录下创建left_arm.txt和right_arm.txt
    for arm_file in ["left_arm.txt", "right_arm.txt"]:
        file_path = os.path.join(sub_directory, arm_file)

        # 将"0 0 0 0 0 0 0"写入每个文件的100行
        with open(file_path, "w") as file:
            for _ in range(100):
                file.write("0 0 0 0 0 0 0\n")