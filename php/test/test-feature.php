<?php

use PHPUnit\Framework\TestCase;

class Feature_Test extends TestCase {

    public function setUp(): void {
		require_once __DIR__ . '/../src/feature.php';
	}

    public function testShouldExecute()
    {
        $objectUnderTest = new Feature();

        $this->assertTrue($objectUnderTest->shouldExecute());
    }
}