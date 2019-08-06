import axios from 'axios'

const API_URL = 'http://localhost:8000/api'

const http = axios.create({
    baseURL: API_URL,
    headers: {
    'Content-Type': 'application/json',
    }
})

http.interceptors.request.use((config) => {
    const token = localStorage.getItem('jwt')

    if (token) {
        config.headers.Authorization = `Token ${token}`
}

    return config
}, (err) => {
    return Promise.reject(err)
})

http.interceptors.response.use((response) => {
    return response
}, (error) => {
    if (error.response.status === 401) {
        window.location = '/'
}

    return Promise.reject(error)
})

export default http