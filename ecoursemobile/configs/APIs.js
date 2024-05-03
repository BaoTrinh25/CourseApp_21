import axios from "axios";
const BASE_URL = "https://thanhduong.pythonanywhere.com/";

export const endpoints = {
    'category': '/categories/',
    'course': '/courses/'
}

export default axios.create({
    baseURL: BASE_URL
});