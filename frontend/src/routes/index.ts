import {createRouter, createWebHistory, type RouteRecordRaw} from "vue-router";
import Home from "@/views/home/Index.vue"
import BBS from "@/views/bbs/threadList/Index.vue"
import BBSDetail from "@/views/bbs/thread/Index.vue"
import OKR from "@/views/okr/Index.vue"
import Login from "@/views/login/LoginForm.vue"
import Register from "@/views/login/RegisterForm.vue"
import ForgotPassword from "@/views/login/ForgotPasswordForm.vue"
import Admin from "@/views/admin/Index.vue"
import User from "@/views/admin/user/Index.vue"
import Role from "@/views/admin/role/Index.vue"
import Interview from "@/views/iv/interview/Index.vue"
import MainLayout from "@/components/layout/MainLayout.vue";
import BlankLayout from "@/components/layout/BlankLayout.vue";
import AdminLayout from "@/components/layout/AdminLayout.vue";

const routes: Array<RouteRecordRaw> = [
    {
        path: '/',
        component: MainLayout,
        children: [
            { path: '', name: 'Home', component: Home },
            { path: 'bbs', name: 'BBS', component: BBS },
            { path: 'bbs/:id', name: 'BBSDetail', component: BBSDetail },
        ],
    },
    {
        path: '/login',
        component: BlankLayout,
        children: [
            { path: '', name: 'Login', component: Login },
        ],
    },
    {
        path: '/register',
        component: BlankLayout,
        children: [
            { path: '', name: 'Register', component: Register },
        ],
    },
    {
        path: '/forgot-password',
        component: BlankLayout,
        children: [
            { path: '', name: 'ForgotPassword', component: ForgotPassword },
        ],
    },
    {
        path: '/okr',
        component: BlankLayout,
        children: [
            { path: '', name: 'OKR', component: OKR },
        ],
    },
    {
        path: '/admin',
        component: AdminLayout,
        children: [
            { path: '', name: 'Admin', component: Admin },
            { path: 'user', name: 'User', component: User },
            { path: 'role', name: 'Role', component: Role },
        ],
    },
    {
        path: '/iv',
        component: AdminLayout,
        children: [
            { path: 'interview', name: 'Interview', component: Interview },
        ]
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router
