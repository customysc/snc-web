import {defineStore} from "pinia";
import {ref} from "vue";
import {loginApi} from "../../views/login/login.api.ts";
import {setAuthCache} from "../auth";
import {TOKEN_KEY} from "../../enums/cacheEnum.ts";

interface UserState {
    userInfo?: any;
    token?: string;
    roleList?: any[];
    loginInfo?: any;
}

export const useUserStore = defineStore('user', () => {
    const userInfo = ref();
    const token = ref();

    function setToken(info?: string) {
        token.value = info ?? ''
        setAuthCache(TOKEN_KEY, info)
    }

    async function login(params) {
        try {
            const res = await loginApi(params);
            console.log(res);
            const data = res.data;
            console.log(data);
            token.value = data.token;
            userInfo.value = data.userInfo;

            setToken(token)
            return data;
        } catch (error) {
            return Promise.reject(error);
        }
    }

    return {
        userInfo,
        token,
        login
    }
})
