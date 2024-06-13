import os
base_directory = "SonnieControl/upbody/ArmControl/file/custom_motion_set"
for i in range(1, 101):
    sub_directory = os.path.join(base_directory, f"motion_{i}")
    waist_file_path = os.path.join(sub_directory, "waist.txt")
    existing_file_path = os.path.join(sub_directory, "left_arm.txt")
    with open(existing_file_path, "r") as existing_file:
        num_lines = sum(1 for line in existing_file)
    with open(waist_file_path, "w") as waist_file:
        for _ in range(num_lines):
            waist_file.write("0 0 0\n")
