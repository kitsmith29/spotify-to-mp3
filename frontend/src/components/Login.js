import Paper from "@mui/material/Paper"
import Box from "@mui/material/Box"
import Typography from "@mui/material/Typography"
import Button from "@mui/material/Button"
import React from 'react'
import Container from "@mui/material/Container"

const styles = {
    container: {
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        marginTop: 30
    },
    paper: {
        border: 3,
    },
    title: {
        padding: 3,
        marginLeft: 5,
        marginRight: 5,
        textAlign: "center"
    },
    image: {
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        width: 80,
        height: 80
    },
    button: {
        borderTop: 3,
        borderRadius: 0,
        borderColor: "white",
        padding: 1,
        backgroundColor: "#009900",
        width: "100%",
        marginTop: 3,
        "&.MuiButton-text": {
            color: "#FFFFFF",
            fontWeight: "bold",
            fontSize: 15
        }
    }
}

function Login() {

    return (
        <Container sx={styles.container}>
            <Paper elevation={10} sx={styles.paper}>
                <Typography variant="h4" sx={styles.title}>
                    Spotify to MP3
                </Typography>
                <Box
                    component="img"
                    sx={styles.image}
                    m="auto"
                    src={require("./images/spotify.png")}
                />
                <Button sx={styles.button}>
                    Login
                </Button>
            </Paper>
        </Container >
    )
}

export default Login