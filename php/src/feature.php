<?php

class Feature {

    public function shouldExecute() {
        if ( rand( 0, 10 ) > 5 ) {
            return true;
        }
        return false;
    }
}

