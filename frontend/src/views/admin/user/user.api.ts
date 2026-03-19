import http from "../../../utils/axios";

export enum Api {
    page = '/sys/user/page',
}

export const userPageApi = (params?) => {
    console.log(params);
    return http.get(Api.page, {params})
};
