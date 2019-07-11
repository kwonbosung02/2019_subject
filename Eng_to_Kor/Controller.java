package org.dimigo.gui.Stack;

import javafx.animation.Animation;
import javafx.animation.KeyFrame;
import javafx.animation.Timeline;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;

import javafx.scene.control.*;

import java.net.URL;

import java.text.SimpleDateFormat;
import java.util.*;

public class Controller implements Initializable {

    @FXML
    TextArea givetext;
    @FXML
    TextArea returntext;


    Date dt = new Date();
    SimpleDateFormat sdf = new SimpleDateFormat("hh:mm:ss", Locale.KOREA);

    HashMap<String,String> map = new HashMap<String, String>( );
    @Override
    public void initialize(URL location, ResourceBundle resources){

    }


    public void handleTranslate(ActionEvent event){
        String give_text = givetext.getText();
        give_text.replace(". ",".\n");

        givetext.setWrapText(true);
        //System.out.println(give_text);
        String a = TranslatorText.giveText( give_text );
        String b ="";
        try {
            b = String.valueOf( TranslatorText.show( a ));
            b.replace(". ",".\n");
        }catch (Exception e){

        }

        returntext.setText( b.replace(". ",".\n") );

    }



}