import axios from "axios";

const api = axios.create({
    baseURL: "https://cinevision-ai-production.up.railway.app",
});

export default api;