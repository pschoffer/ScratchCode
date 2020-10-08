<?php

use PHPUnit\Framework\TestCase;

class Feature_Test extends TestCase {

    public function setUp(): void {
		require_once __DIR__ . '/../src/feature.php';
	}

    public function provideDataShouldExecute() {
        return [
            [9, true],
            [1, false]
        ];
    }

    /**
    * @dataProvider provideDataShouldExecute
    */
    public function testShouldExecute( $randomValue, $expectedResult)
    {
        $objectUnderTest = new Feature();

        $objectUnderTest->dependency = $this->createMock( Dependency::class );

        $objectUnderTest->dependency->method( 'random' )->willReturn( $randomValue );

        $this->assertEquals( $expectedResult, $objectUnderTest->shouldExecute() );
    }
}