import Container from "react-bootstrap/Container";
import Navbar from "react-bootstrap/Navbar";
import "./Navigation.css";

function NavTop() {
  const handleSelect = (eventKey) => alert(`selected ${eventKey}`);

  return (
    <Navbar bg="light" sticky="top">
      <Container>
        <Navbar.Brand href="/">チャンカリ</Navbar.Brand>
      </Container>
    </Navbar>
  );
}

//render(<NavDropdownExample />);
export default NavTop;
