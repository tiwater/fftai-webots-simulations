import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt


# 读取文本文件
data = np.loadtxt('/home/fugo/fsa_all_version/release_v1/gr1-fsa/SonnieControl/upbody/ArmControl/file/gtc_dance/all_pos.txt')
# waist_data = np.loadtxt('/home/fugo/fsa_all_version/release_v1/gr1-fsa/SonnieControl/upbody/ArmControl/file/gtc_dance/adjusted_data.txt')

# 打印读取的数据
print(data.shape)

left_arm = data[:, 25:29]
# zero_columns = np.zeros((left_arm.shape[0], 3))
# new_left_arm = np.hstack((left_arm, zero_columns))
right_arm = data[:, 32:36]
# zero_columns = np.zeros((left_arm.shape[0], 3))
# new_right_arm = np.hstack((right_arm, zero_columns))

waist = data[:, 1] 
waist = waist + np.abs(waist[0])



# 创建一些示例数据
x = np.linspace(1, len(waist), len(waist))


# 创建三次插值函数
interpolation_function1 = interp1d(x, waist, kind='cubic', fill_value='extrapolate')
interpolation_function2 = interp1d(x, left_arm[:,0], kind='cubic', fill_value='extrapolate')
interpolation_function3 = interp1d(x, left_arm[:,1], kind='cubic', fill_value='extrapolate')
interpolation_function4 = interp1d(x, left_arm[:,2], kind='cubic', fill_value='extrapolate')
interpolation_function5 = interp1d(x, left_arm[:,3], kind='cubic', fill_value='extrapolate')
interpolation_function6 = interp1d(x, right_arm[:,0], kind='cubic', fill_value='extrapolate')
interpolation_function7 = interp1d(x, right_arm[:,1], kind='cubic', fill_value='extrapolate')
interpolation_function8 = interp1d(x, right_arm[:,2], kind='cubic', fill_value='extrapolate')
interpolation_function9 = interp1d(x, right_arm[:,3], kind='cubic', fill_value='extrapolate')

# 生成新的插值点
new_x = np.linspace(1, len(waist), len(waist)*15)


new_left_arm = np.random.rand(len(waist)*15, 4)
new_right_arm = np.random.rand(len(waist)*15, 4)

new_waist = interpolation_function1(new_x)
new_left_arm[:,0] = interpolation_function2(new_x)
new_left_arm[:,1] = interpolation_function3(new_x)
new_left_arm[:,2] = interpolation_function4(new_x)
new_left_arm[:,3] = interpolation_function5(new_x)
new_right_arm[:,0] = interpolation_function6(new_x)
new_right_arm[:,1] = interpolation_function7(new_x)
new_right_arm[:,2] = interpolation_function8(new_x)
new_right_arm[:,3] = interpolation_function9(new_x)


new_left_arm[:,0] = - new_left_arm[:,0] 
new_left_arm[:,1] = - new_left_arm[:,1]*0.6
new_left_arm[:,3] = - new_left_arm[:,3] 
new_left_arm[:,2] = 0


new_right_arm[:,1] = - new_right_arm[:,1]*0.6

for i in range(len(new_left_arm)):
    if(new_left_arm[i,3] < 0):
        new_left_arm[i,3] = -new_left_arm[i,3]


zero_columns = np.zeros((new_left_arm.shape[0], 3))
new_left_arm = np.hstack((new_left_arm, zero_columns))

zero_columns = np.zeros((new_right_arm.shape[0], 3))
new_right_arm = np.hstack((new_right_arm, zero_columns))

# 绘制原始数据和插值结果
plt.scatter(x, left_arm[:,0], label='Original Data')
plt.plot(new_x, new_left_arm[:,0], label='Interpolated Data (Cubic)')
plt.legend()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Cubic Interpolation')
plt.show()





np.savetxt('/home/fugo/fsa_all_version/release_v1/gr1-fsa/SonnieControl/upbody/ArmControl/file/gtc_dance/new_left_arm.txt', new_left_arm, fmt='%f', delimiter=' ')
np.savetxt('/home/fugo/fsa_all_version/release_v1/gr1-fsa/SonnieControl/upbody/ArmControl/file/gtc_dance/new_right_arm.txt', new_right_arm, fmt='%f', delimiter=' ')
np.savetxt('/home/fugo/fsa_all_version/release_v1/gr1-fsa/SonnieControl/upbody/ArmControl/file/gtc_dance/waist.txt', new_waist, fmt='%f', delimiter=' ')


