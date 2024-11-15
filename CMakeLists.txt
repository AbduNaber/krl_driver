cmake_minimum_required(VERSION 3.5)
project(krl_driver)

# Default to C99
if(NOT CMAKE_C_STANDARD)
  set(CMAKE_C_STANDARD 99)
endif()

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(serial REQUIRED)
find_package(yaml-cpp REQUIRED)


include_directories(include ${serial_INCLUDE_DIRS})
include_directories(/home/gturover/anadolu_ws/src/serial-ros2/include)
add_executable(krl_driver src/krl_driver.cpp)
ament_target_dependencies(krl_driver rclcpp std_msgs geometry_msgs )
target_link_libraries(krl_driver ${serial_LIBRARIES} yaml-cpp)
target_include_directories(
  krl_driver PUBLIC $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
                    $<INSTALL_INTERFACE:include>)

install(TARGETS krl_driver DESTINATION lib/${PROJECT_NAME})
install(DIRECTORY launch params DESTINATION share/${PROJECT_NAME}/)

ament_package()
