import logo from "./logo.svg";
import "./App.css";
import { Container, TextField } from "@material-ui/core";
import { useState } from "react";

function makeid(length) {
  var result           = '';
  var characters       = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
  var charactersLength = characters.length;
  for ( var i = 0; i < length; i++ ) {
     result += characters.charAt(Math.floor(Math.random() * charactersLength));
  }
  return result;
}


function App() {
  const [uid, setuid] = useState("");
  if (localStorage.getItem("uid") === null || localStorage.getItem("uid") === "" ) {
    setuid(makeid(10));
    localStorage.setItem("uid", uid);
  }
  localStorage.setItem("piss", "poss")

  return (
    <Container>
      <form noValidate autoComplete="off">
        <TextField id="filled-basic" label="Filled" variant="filled" />
      </form>

      <button onClick={(e)=>{
        localStorage.removeItem("uid");
      }}>
        click to reset the storage
      </button>
      {localStorage.getItem("uid")}
    </Container>
  );
}

export default App;
