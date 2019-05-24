package br.insper.robot19.vrep;

import br.insper.robot19.*;

public class MainGulosa {
    public static void main(String[] args) {

        float cellsize = 0.5f;

        VrepSimulator sim = VrepSimulator.getInstance();
        VrepWorld world = sim.createWorld();
        VrepRobot robot = sim.createRobot();
        GridMap map = world.buildMap(cellsize);

        float[] xyIni = robot.getPosition();

        int[] rowColIni = map.gridRowCol(xyIni[0], xyIni[1]);
        int[] rowColFim = map.getGoal();
        Block inicial = new Block(rowColIni[0], rowColIni[1], BlockType.FREE);
        Block alvo = new Block(rowColFim[0], rowColFim[1], BlockType.FREE);
        BuscaGulosa busca = new BuscaGulosa(map, inicial, alvo);
        RobotAction[] solucao = busca.resolver();

        System.out.println(map);

        if (solucao == null) {
            System.out.println("Nao foi encontrada solucao para o problema");
        } else {

            Block atual = inicial;
            System.out.print("Solução: ");
            for (RobotAction a : solucao) {
                System.out.print(", " + a);
                Block next = map.nextBlock(atual, a);
                map.setRoute(next.row, next.col);
                atual = next;
            }

            //Mostra o mapa com a rota encontrada
            System.out.println();
            System.out.println("Rota encontrada:");
            System.out.println(map);

            for (RobotAction a: solucao) {
                robot.execute(a, cellsize);
            }
        }
    }
}
