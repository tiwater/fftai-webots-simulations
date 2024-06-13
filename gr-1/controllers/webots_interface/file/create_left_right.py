import os
base_directory = "SonnieControl/upbody/ArmControl/file/custom_motion_set"
for i in range(1, 101):
    sub_directory = os.path.join(base_directory, f"motion_{i}")
    os.makedirs(sub_directory)
    for arm_file in ["left_arm.txt", "right_arm.txt"]:
        file_path = os.path.join(sub_directory, arm_file)
        with open(file_path, "w") as file:
            for _ in range(100):
                file.write("0 0 0 0 0 0 0\n")