# 代码生成时间: 2025-09-24 00:03:57
import requests

"""
用户权限管理系统

该程序使用requests框架与后端API交互，实现用户权限的管理。
包括用户权限的添加、删除、更新和查询功能。
"""

class UserPermissionManagement:
    def __init__(self, base_url):
        """初始化API的基础URL"""
        self.base_url = base_url

    def add_permission(self, user_id, permission):
        """添加用户权限"""
        url = f"{self.base_url}/users/{user_id}/permissions"
        data = {"permission": permission}
        try:
            response = requests.post(url, json=data)
            response.raise_for_status()
            return {"status": "success", "message": "Permission added successfully"}
        except requests.RequestException as e:
            return {"status": "error", "message": str(e)}

    def remove_permission(self, user_id, permission):
        """移除用户权限"""
        url = f"{self.base_url}/users/{user_id}/permissions/{permission}"
        try:
            response = requests.delete(url)
            response.raise_for_status()
            return {"status": "success", "message": "Permission removed successfully"}
        except requests.RequestException as e:
            return {"status": "error", "message": str(e)}

    def update_permission(self, user_id, old_permission, new_permission):
        """更新用户权限"""
        url = f"{self.base_url}/users/{user_id}/permissions/{old_permission}"
        data = {"permission": new_permission}
        try:
            response = requests.put(url, json=data)
            response.raise_for_status()
            return {"status": "success", "message": "Permission updated successfully"}
        except requests.RequestException as e:
            return {"status": "error", "message": str(e)}

    def get_permissions(self, user_id):
        """获取用户权限列表"""
        url = f"{self.base_url}/users/{user_id}/permissions"
        try:
            response = requests.get(url)
            response.raise_for_status()
            return {"status": "success", "data": response.json()}
        except requests.RequestException as e:
            return {"status": "error", "message": str(e)}

# 示例用法
if __name__ == "__main__":
    base_url = "http://example.com/api"
    manager = UserPermissionManagement(base_url)
    # 添加权限
    print(manager.add_permission(1, "read"))
    # 移除权限
    print(manager.remove_permission(1, "write"))
    # 更新权限
    print(manager.update_permission(1, "edit", "delete"))
    # 获取权限列表
    print(manager.get_permissions(1))