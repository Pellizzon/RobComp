package br.insper.robot19;

public class Node {
	private Block value;
	private Node parent;
	private RobotAction action;
	private float pathCost;
	private int heuristic;

	public Node(Block value, Node parent, RobotAction action, float cost, GridMap map) {
		this.value = value;
		this.parent = parent;
		this.action = action;

		int[] finish = map.getGoal();

		this.heuristic = Math.abs(finish[0] - value.row) + Math.abs(finish[1] - value.col);
		this.pathCost = parent == null ? 0 : parent.getPathCost() + cost;
	}

	public int getHeuristic() {
		return heuristic;
	}

	public Block getValue() {
		return value;
	}
	
	public Node getParent() {
		return parent;
	}
	
	public RobotAction getAction() {
		return action;
	}
	
	public float getPathCost() {
		return pathCost;
	}

}
