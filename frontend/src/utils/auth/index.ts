import {type BasicKeys, Persistent} from "../cache/persistent.ts";

export function setAuthCache(key: BasicKeys, value) {
    const fn = Persistent.setLocal;
    return fn(key, value, true);
}
