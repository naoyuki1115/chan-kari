
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Alert from 'react-bootstrap/Alert';
import Card from 'react-bootstrap/Card';
function RentList() {
    return (
        <Container>

            <h3>貸しているものリスト</h3>
            <Row xs={1} md={2} className="g-4">
                {Array.from({ length: 8 }).map((_, idx) => (
                    <Col>
                        <Card>
                            <Card.Img variant="top" src="https://placehold.jp/100x40.png" />
                            <Card.Body>
                                <Card.Title>レンタル品</Card.Title>
                                <Card.Text>
                                    【貸出者：○○○】
                                </Card.Text>
                            </Card.Body>
                        </Card>
                    </Col>
                ))}
            </Row>
        </Container>
    );
};

export default RentList;