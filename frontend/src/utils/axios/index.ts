import axios from 'axios';

const http = axios.create({
    baseURL: '', // 更改为后端API地址
    timeout: 2000,
    withCredentials: true,
    headers: {
        'Content-Type': 'application/json'
    }
});

export default http;
