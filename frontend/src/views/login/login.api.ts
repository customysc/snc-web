import http from "../../utils/axios";

export enum Api {
    login = '/sys/login',
}

export const loginApi = (params?) => http.post(Api.login, params);
