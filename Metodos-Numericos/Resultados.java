class Resultados {
    /**
     * @param args
     */
    public static void main(String[] args) {

        int t = 0;
        double gra = 9.8;
        double masa = 62;
        double c_resis = 12.5; 
        System.out.println("Solucion Analitica o Exacta");
        for(int i = 0; i < 100; i++) {
            System.out.println(i*2+"- "+((gra*masa)/c_resis)*(1-Math.exp(-(c_resis/masa)*t)));
            t = t+2;
        }
        
        t=2;
        float velocidad=0;
        System.out.println("\nSolucion Numerica");
        for( int i = 0; i < 100; i++) {
            System.out.println(i*2+"- "+velocidad);
            velocidad = (float) (gra-((c_resis*velocidad)/masa))*t+velocidad;
        }
        
    }

    
}

