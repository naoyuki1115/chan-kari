import {
  Routes,
  Route,
  useNavigationType,
  useLocation,
} from "react-router-dom";
import Component from "./pages/Component";
import Component3 from "./pages/Component3";
import Component4 from "./pages/Component4";
import Component5 from "./pages/Component5";
import Component6 from "./pages/Component6";
import Component7 from "./pages/Component7";
import Component8 from "./pages/Component8";
import Component9 from "./pages/Component9";
import Component10 from "./pages/Component10";
import Component11 from "./pages/Component11";
import Component12 from "./pages/Component12";
import Component13 from "./pages/Component13";
import { useEffect } from "react";

function App() {
  const action = useNavigationType();
  const location = useLocation();
  const pathname = location.pathname;

  useEffect(() => {
    if (action !== "POP") {
      window.scrollTo(0, 0);
    }
  }, [action]);

  useEffect(() => {
    let title = "";
    let metaDescription = "";

    //TODO: Update meta titles and descriptions below
    switch (pathname) {
      case "/":
        title = "";
        metaDescription = "";
        break;
      case "/1":
        title = "";
        metaDescription = "";
        break;
      case "/8":
        title = "";
        metaDescription = "";
        break;
      case "/2":
        title = "";
        metaDescription = "";
        break;
      case "/5":
        title = "";
        metaDescription = "";
        break;
      case "/4":
        title = "";
        metaDescription = "";
        break;
      case "/3":
        title = "";
        metaDescription = "";
        break;
      case "/7":
        title = "";
        metaDescription = "";
        break;
      case "/6":
        title = "";
        metaDescription = "";
        break;
      case "/9":
        title = "";
        metaDescription = "";
        break;
      case "/":
        title = "";
        metaDescription = "";
        break;
      case "/10":
        title = "";
        metaDescription = "";
        break;
    }

    if (title) {
      document.title = title;
    }

    if (metaDescription) {
      const metaDescriptionTag: HTMLMetaElement | null = document.querySelector(
        'head > meta[name="description"]'
      );
      if (metaDescriptionTag) {
        metaDescriptionTag.content = metaDescription;
      }
    }
  }, [pathname]);

  return (
    <Routes>
      <Route path="/" element={<Component />} />

      <Route path="/1" element={<Component3 />} />

      <Route path="/8" element={<Component4 />} />

      <Route path="/2" element={<Component5 />} />

      <Route path="/5" element={<Component6 />} />

      <Route path="/4" element={<Component7 />} />

      <Route path="/3" element={<Component8 />} />

      <Route path="/7" element={<Component9 />} />

      <Route path="/6" element={<Component10 />} />

      <Route path="/9" element={<Component11 />} />

      <Route path="/" element={<Component12 />} />

      <Route path="/10" element={<Component13 />} />
    </Routes>
  );
}
export default App;
