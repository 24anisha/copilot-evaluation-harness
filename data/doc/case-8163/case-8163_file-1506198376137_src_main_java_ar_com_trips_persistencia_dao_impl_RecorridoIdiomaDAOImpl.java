package ar.com.trips.persistencia.dao.impl;

import java.util.List;

import org.hibernate.Session;
import org.springframework.transaction.annotation.Transactional;

import ar.com.trips.persistencia.dao.IRecorridoIdiomaDAO;
import ar.com.trips.persistencia.modelo.Recorrido;
import ar.com.trips.persistencia.modelo.RecorridoIdioma;

public class RecorridoIdiomaDAOImpl extends DAOImpl implements IRecorridoIdiomaDAO {

	@Override
	public List<RecorridoIdioma> listarPorCiudad(int idCiudad, String idioma) {
		Session session = sessionFactory.openSession();
		String query = "FROM " + Recorrido.class.getName() + " a WHERE a.ciudad.id = " + idCiudad 
					+ " AND a.idioma = '" + idioma + "' AND a.borrado = 0";
		@SuppressWarnings("unchecked")
		List<RecorridoIdioma> lista = session.createQuery(query).list();
		session.close();
		return lista;
	}

	@Transactional
	public void borrar(long id) {
		Session s = sessionFactory.openSession();
		s.beginTransaction();
		RecorridoIdioma model = (RecorridoIdioma) s.get(RecorridoIdioma.class, id);
		model.setBorrado(1);
		s.update(model);
		s.getTransaction().commit();
		s.close();
	}

	@Override
	public RecorridoIdioma get(Long id) {
		return this.get(RecorridoIdioma.class, id);
	}

	@Override
	public RecorridoIdioma get(Long idRecorrido, String idioma) {
		Session session = sessionFactory.openSession();
		String query = "FROM " + RecorridoIdioma.class.getName() + " a WHERE a.recorrido.id = " + idRecorrido 
				+ " AND a.idioma = '" + idioma + "' AND a.borrado = 0";
		@SuppressWarnings("unchecked")
		List<RecorridoIdioma> lista = session.createQuery(query).list();
		session.close();
		if (lista.size() == 0) {
			return null;
		} else {
			return lista.get(0);
		}
	}
}