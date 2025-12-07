const express = require('express');
const cors = require('cors');
const dotenv = require('dotenv');

// 환경변수 로드
dotenv.config();

const app = express();
const PORT = process.env.PORT || 5000;

// 미들웨어 설정
app.use(cors());    // 프론트엔드 요청 허용
app.use(express.json());    // JSON 요청 파싱

// 테스트 라우트
app.get('/', (req, res) => {
    res.json({ message: 'Linkdo API is running'});
});

// 서버 시작
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
