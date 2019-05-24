package br.insper.robot19;

import java.util.*;

public class BuscaA {

    private Block start;
    private Block end;
    private GridMap map;

    private Animacao desenho;
    private int contador = 1;

    private PriorityQueue<Node> border;

    public BuscaA(GridMap map, Block start, Block end) {
        this.map = map;
        this.start = start;
        this.end = end;
        this.desenho = new Animacao(map);
        this.desenho.desenha();
        this.desenho.saveFile("AnimacaoBuscaA0.png");
    }

    public Node buscar() {

        Node root = new Node(start, null, null, 0, map);

        border = new PriorityQueue<Node>(144, new ComparatorA());
        border.add(root);

        Set<Block> visitados = new HashSet<>();
        visitados.add(root.getValue());

        while(!border.isEmpty()) {

            Node node = border.remove();
            Block atual = node.getValue();
            visitados.add(atual);

            if(atual.row == end.row && atual.col == end.col) {
                desenho.desenha_visitado(atual);
                return node;

            } else for(RobotAction acao : RobotAction.values()) {

                Block proximo = map.nextBlock(atual, acao);

                if(proximo != null && proximo.type != BlockType.WALL) {
                    Node novoNode = new Node(proximo, node, acao, proximo.type.cost, map);
                    if (!visitados.contains(novoNode.getValue())) {
                        border.add(novoNode);
                        desenho.desenha_fronteira(novoNode.getValue());
                    }
                }
                desenho.desenha_visitado(atual);
            }
            desenho.saveFile("AnimacaoBuscaA" + contador + ".png");
            contador++;
        }
        return null;
    }

    public RobotAction[] resolver() {

        // Encontra a solução através da busca
        Node destino = buscar();
        if(destino == null) {
            return null;
        }

        //Faz o backtracking para recuperar o caminho percorrido
        Node atual = destino;
        Deque<RobotAction> caminho = new LinkedList<RobotAction>();
        while(atual.getAction() != null) {
            caminho.addFirst(atual.getAction());
            atual = atual.getParent();
        }
        desenho.setAndDrawSolucao(caminho.toArray(new RobotAction[caminho.size()]));
        desenho.saveFile("ResolucãoBuscaA.png");
        return caminho.toArray(new RobotAction[caminho.size()]);
    }
}
