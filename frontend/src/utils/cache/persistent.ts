import { toRaw } from 'vue';
import {
    TOKEN_KEY,
    USER_INFO_KEY,
    ROLES_KEY,
    LOCK_INFO_KEY,
    DB_DICT_DATA_KEY,
    LOGIN_INFO_KEY,
} from '../../enums/cacheEnum.ts';
import type {LoginInfo, UserInfo} from "../../../types/store";
import {createLocalStorage, createSessionStorage, DEFAULT_CACHE_TIME} from "./index.ts";
import {APP_LOCAL_CACHE_KEY} from "../../enums/cacheEnum.ts";
import { Memory } from './memory';

interface BasicStore {
    [TOKEN_KEY]: string | number | null | undefined;
    [USER_INFO_KEY]: UserInfo;
    [ROLES_KEY]: string[];
    [LOCK_INFO_KEY]: LockInfo;
    [DB_DICT_DATA_KEY]: string;
    [LOGIN_INFO_KEY]: LoginInfo;
}

export type BasicKeys = keyof BasicStore;
type LocalStore = BasicStore;
type LocalKeys = keyof LocalStore;

const ls = createLocalStorage();
const ss = createSessionStorage();

const localMemory = new Memory(DEFAULT_CACHE_TIME);

export class Persistent {
    // static getLocal<T>(key: LocalKeys) {
    //     const globalCache = ls.get(APP_LOCAL_CACHE_KEY);
    //     if (globalCache && router?.currentRoute?.value.path !== PageEnum.BASE_LOGIN) {
    //         localMemory.setCache(globalCache);
    //     }
    //     return localMemory.get(key)?.value as Nullable<T>;
    // }


    static setLocal(key: LocalKeys, value: LocalStore[LocalKeys], immediate = false): void {
        localMemory.set(key, toRaw(value));
        immediate && ls.set(APP_LOCAL_CACHE_KEY, localMemory.getCache);
    }

    static removeLocal(key: LocalKeys, immediate = false): void {
        localMemory.remove(key);
        immediate && ls.set(APP_LOCAL_CACHE_KEY, localMemory.getCache);
    }

    static clearLocal(immediate = false): void {
        localMemory.clear();
        immediate && ls.clear();
    }

    static clearAll(immediate = false) {
        localMemory.clear();
        if (immediate) {
            ls.clear();
            ss.clear();
        }
    }
}
