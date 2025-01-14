

#define SET(x,mask) x=(mask)
#define SET1(x,mask) x|=(mask)
#define SET0(x,mask) x&=~(mask)
#define REV(x,mask) x^=(mask)

void delay(int t) {
	int i;
	for (i = 0; i < t; i++);
}





// ------------- DISPLAY -------------
#define page_start 0xB8
#define column_start 0x40


void strob(void) {
	SET1(PF_ODR, 0x80);
	delay(1);
	SET0(PF_ODR, 0x80);
}

void display_init(void) {
	// порты
	PB_DDR = 0xFF;
	PB_CR1 = 0xFF;
	PB_CR2 = 0xFF;
	PF_DDR = 0xFF;
	PF_CR1 = 0xFF;
	PF_CR2 = 0xFF;
	
	// инициализация
	PF_ODR = 0x00;
	delay(1);
	SET1(PF_ODR, 0x10);
	delay(10);
	SET1(PF_ODR, 0x09);
	PB_ODR = 0x3F;
	strob();
}

char page_buf[64][8]
void draw_page_buf(void) {
    int i;
    // кристал 1
	SET1(PF_ODR, 0x01);
	SET0(PF_ODR, 0x08);
    // выбор страницы
    SET(PB_ODR, page_start);
    strob();
    // выбор колонки
    SET(PB_ODR, column_start);
    strob();
    //начать запись
    SET1(PF_ODR, 0x40);
    for (i = 0; i < 64; i++) {
        SET(PB_ODR, page_buf[i]);
        strob();
    }
    // закончить запись
    SET0(PF_ODR, 0x40);
}





// ------------- TIMER -------------
void shim_init(void) {
    // TIM1
    SET0(TIM1_CCMR1, 0x03);
    SET0(TIM1_CCMR1, 0x04);
    SET1(TIM1_CCMR1, 0x08);
    SET1(TIM1_CCMR1, 0x60);
    SET1(TIM1_CCER1, 0x01);
    SET1(TIM1_BKR, 0x80);
    // 1 кГц (делитель частоты)
    SET(TIM1_PSCRH,0x07);
    SET(TIM1_PSCRL,0xCF);
    // 10 (автоперегрузка)
    SET(TIM1_ARRH, 0x00);
    SET(TIM1_ARRL, 0x09);
    // 5 (регистр захвата)
    SET(TIM1_CCR1H, 0x00);
    SET(TIM1_CCR1L, 0x05);
    // вкл
    SET(TIM1_CR1, 0x01);
}