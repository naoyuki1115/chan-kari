import Card from "react-bootstrap/Card";
import Col from "react-bootstrap/Col";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import { Link } from "react-router-dom";

function MyItemList() {
  return (
    <Container>
      <h3>登録品リスト</h3>
      <Row xs={1} md={3} className="g-4">
        {Array.from({ length: 8 }).map((_, idx) => (
          <Col>
            <Card>
              <Card.Img variant="top" src="https://placehold.jp/100x40.png" />
              <Card.Body>
                <Card.Title>レンタル品</Card.Title>
                <Card.Text>
                  <p>貸出OKor貸出中</p>
                  <Link
                    to={"/ItemDetail/BookID"}
                    state={{ fromPage: "MyItemList" }}
                  >
                    詳細
                  </Link>
                </Card.Text>
              </Card.Body>
            </Card>
          </Col>
        ))}
      </Row>
    </Container>
  );
}

export default MyItemList;
