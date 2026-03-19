export interface UserInfo {
    id: string | number;
    userId: string | number;
    username: string;
    realname: string;
    avatar: string;
    desc?: string;
    homePath?: string;
    roles: RoleInfo[];
    orgCode?: string;
}

export interface LoginInfo {
    multi_depart?: string | number;
    userInfo?: object;
    departs?: [];
    isLogin?: boolean;
}
