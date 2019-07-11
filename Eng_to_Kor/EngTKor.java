package org.dimigo.gui.Stack;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;

public class EngTKor extends Application {
    public static void main(String[] args) {

        launch( args );

    }

    public void  start(Stage stage) throws Exception {
        Parent root = FXMLLoader.load( getClass().getResource( "sample.fxml" ) );
        stage.setScene( new Scene(root) );
        stage.setTitle("Novel Translator");

        //stage.centerOnScreen();
        stage.show();

    }


}
