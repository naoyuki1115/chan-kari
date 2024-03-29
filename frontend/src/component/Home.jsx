import Alert from "react-bootstrap/Alert";
import Card from "react-bootstrap/Card";
import Col from "react-bootstrap/Col";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import { Link } from "react-router-dom";

function Home() {
  return (
    <Container>
      <Row>
        <Col>
          <Alert key="dark" variant="dark">
            自分のものを貸したり、友達のものを貸したりしよう
          </Alert>
        </Col>
      </Row>
      <h3>レンタル可能品一覧</h3>
      <Row xs={1} md={3} className="g-4">
        {Array.from({ length: 8 }).map((_, idx) => (
          <Col>
            <Card>
              <Card.Img variant="top" src="https://placehold.jp/100x40.png" />
              <Card.Body>
                <Card.Title>レンタル品</Card.Title>
                <Card.Text>
                  <p>【貸出者：○○○】</p>
                  <Link
                    to={"/ItemDetail/BookID"}
                    state={{ fromPage: "HomePage" }}
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

export default Home;
