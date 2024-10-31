using System.Collections.Generic;
using System.Linq;
using EX2.Models;

namespace EX2
{
    public class StateMachine
    {
        #region Protected Properties

        protected Graph Graph = new Graph();

        #endregion

        #region Private Properties

        protected string CurrentState;

        #endregion

        #region Private Methods

        private string Step(string to, string edge)
        {
            var node = Graph.States.First(x => x.Name == to);
            return node.Edges.FirstOrDefault(x => x.Name == edge).Node.Name;
        }

        #endregion

        #region Public Methods

        public StateMachine()
        {
            #region States

            var states = new List<State>();
            var state1 = new State("S1");
            var state2 = new State("S2");
            var state3 = new State("S3");
            var state4 = new State("S4");

            #endregion

            #region Edges

            state1.Edges.Add(new Edge("a", state2));

            state2.Edges.Add(new Edge("a", state2));
            state2.Edges.Add(new Edge("b", state1));
            state2.Edges.Add(new Edge("c", state4));

            state3.Edges.Add(new Edge("a", state1));
            state3.Edges.Add(new Edge("b", state4));

            state4.Edges.Add(new Edge("d", state3));

            #endregion

            #region Graph

            Graph.States.Add(state1);
            Graph.States.Add(state2);
            Graph.States.Add(state3);
            Graph.States.Add(state4);

            #endregion

            //Start Node
            this.CurrentState = "S1";
        }

        public string Run(IEnumerable<string> Steps)
        {
            foreach (var item in Steps)
            {
                this.CurrentState = Step(this.CurrentState, item);
            }
            return this.CurrentState;
        }

        #endregion
    }
}