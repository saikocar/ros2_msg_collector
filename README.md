# ros2_msg_collector

メッセージ定義ファイルを含むパッケージだけを抽出するスクリプト

## 使い方

```bash
python3 main.py <path/to/workspace/src>
```

### レインボーで使う例

`sftp://192.168.1.21` をマウントしてから下記を実行
```bash
python3 main.py '/run/user/1000/gvfs/sftp:host=192.168.1.21/home/sit/ros2_rainbow/src'
```

メッセージをビルドする
```bash
cd `ls -dt */ | head -1`
rm -r src/planning_validator src/control_performance_analysis src/planning_debug_tools src/dummy_perception_publisher src/control_validator src/operation_mode_transition_manager src/static_centerline_optimizer src/vehicle_cmd_gate src/yabloc_particle_filter
rosdep update
rosdep install -y --from-paths src --ignore-src --rosdistro $ROS_DISTRO
colcon build --symlink-install --cmake-args -DCMAKE_BUILD_TYPE=Release
```
