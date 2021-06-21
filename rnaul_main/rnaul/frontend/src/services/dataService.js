import http from '../http-common';

class DataService {
    getToxicScore(data){
        console.log(data);
        return http.post('/toxicity', data);
    }
}
export default new DataService();
