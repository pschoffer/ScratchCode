<?php

class Feature {

    public function shouldExecute() {
        if ( $this->random() > 5 ) {
            return true;
        }
        return false;
    }

    public function random() {
        return rand( 0, 10 );
    }
}

