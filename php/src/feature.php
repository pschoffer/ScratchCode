<?php

class Dependency {
    public function random() {
        return rand( 0, 10 );
    }
}

class Feature {
    function __construct() {
        $this->dependency = new Dependency();
    }

    public $dependency;

    public function shouldExecute() {
        if ( $this->dependency->random() > 5 ) {
            return true;
        }
        return false;
    }
}

