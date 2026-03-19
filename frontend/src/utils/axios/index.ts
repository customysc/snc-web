import axios from 'axios';

const http = axios.create({
    baseURL: 'http://127.0.0.1:8000/api/v1', // 更改为后端API地址
    timeout: 2000,
    withCredentials: true,
    headers: {
        'Content-Type': 'application/json'
    }
});

export default http;
