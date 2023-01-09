
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';
function ItemRegister() {
    return (
        <Container>

            <h3>アイテム登録</h3>
            <Row>
                <Form>

                    <Form.Group className="mb-3" controlId="Form.Titlearea1">
                        <Form.Label>タイトル</Form.Label>
                        <Form.Control as="textarea" rows={1} placeholder="タイトル" />
                    </Form.Group>

                    <Form.Group className="mb-3" controlId="Form.Authorarea1">
                        <Form.Label>著者</Form.Label>
                        <Form.Control as="textarea" rows={1} placeholder="著者" />
                    </Form.Group>

                    <Form.Group className="mb-3" controlId="Form.Explainarea1">
                        <Form.Label>Book説明</Form.Label>
                        <Form.Control as="textarea" rows={3} placeholder="説明" />
                    </Form.Group>


                    <Button variant="primary" type="submit">
                        Submit
                    </Button>
                </Form>
            </Row>
        </Container>
    );
};

export default ItemRegister;