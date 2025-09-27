# Claude Code 프로젝트 설정

## Git 커밋 규칙
- 파일 수정 시 자동으로 git commit & push
- 커밋 메시지 형식: `fix:claude+ 날짜 + 시간 + 수정내용 간략하게`
- 예시: `fix:claude+2025-09-27 14:30 add robot controllers to launch file`

## 프로젝트 정보
- ROS1 Practice 프로젝트
- Yahboom X3plus 로봇 시뮬레이션
- Gazebo 환경에서 로봇 제어

## 개발 환경
- **Windows**: 코드 수정만 (Claude Code 사용)
- **Ubuntu VMware**: 실제 ROS 실행 및 테스트
- 주의: Windows에서는 ROS 명령어 실행 불가, 코드 수정만 진행

## 주요 파일들
- `src/my_robot/launch/yahboomcar_gazebo.launch` - 메인 launch 파일
- `src/my_robot/config/control.yaml` - 컨트롤러 설정
- `src/my_robot/urdf/yahboomcar_X3plus.gazebo` - Gazebo 플러그인 설정

## 로봇 제어 명령어
```bash
# 로봇 전진
rostopic pub /yahboomcar/cmd_vel geometry_msgs/Twist "linear: {x: 0.5}" "angular: {z: 0.0}"

# 로봇 회전
rostopic pub /yahboomcar/cmd_vel geometry_msgs/Twist "linear: {x: 0.0}" "angular: {z: 0.5}"
```

## 최근 수정사항
- yahboomcar_gazebo.launch에 컨트롤러 추가 (joint_state_controller, arm_position_controller, gripper_position_controller)
- 중복된 robot_state_publisher 노드 제거