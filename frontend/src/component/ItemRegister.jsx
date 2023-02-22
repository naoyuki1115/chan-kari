
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';
import Modal from 'react-bootstrap/Modal';
import React from 'react';

function ItemRegister() {
    const [modalShow, setModalShow] = React.useState(false);
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



                    <Button variant="primary" onClick={() => setModalShow(true)}>
                        登録
                    </Button>

                    <MyVerticallyCenteredModal
                        show={modalShow}
                        onHide={() => setModalShow(false)}
                    />


                </Form>
            </Row>
        </Container>
    );
};

function MyVerticallyCenteredModal(props) {
    return (
        <Modal
            {...props}
            size="lg"
            aria-labelledby="contained-modal-title-vcenter"
            centered
        >
            <Modal.Header closeButton>
                <Modal.Title id="contained-modal-title-vcenter">
                    登録確認
                </Modal.Title>
            </Modal.Header>
            <Modal.Body>
                <h4>タイトル</h4>
                <p>
                    内容
                </p>
            </Modal.Body>
            <Modal.Footer>
                <Button>登録</Button>
                <Button onClick={props.onHide}>Close</Button>
            </Modal.Footer>
        </Modal>
    );
}








export default ItemRegister;